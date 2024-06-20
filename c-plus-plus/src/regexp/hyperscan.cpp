#include <iostream>
#include <string>
#include <chrono>
#include <vector>
#include <fstream>
#include <filesystem>
#include "hs.h"
#include "database.h"
#include "scratch.h"

const size_t N_REGEX_ITERATIONS = 1000;
const size_t N_CHUNKS_ITERATIONS = 10;

const std::vector<std::string> rules = {
    std::string("[Hh]ello [Ww]orld[!]?"),
    std::string("[Hh]ello [Ww]orld[!]?$"),
    std::string("[0-9][0-9][0-9][0-9][0-9]"),
    std::string("[0-9][0-9][0-9][0-9][0-9]$"),
    std::string("[CV]V[a-z]askjdvc[a-z0-9A-Z]"),
    std::string("^[0-9][0-9]\\.[0-9][0-9]\\.[0-9][0-9]\\.[0-9][0-9]\\s[a-zA-Z]"),
    std::string("^z.*$"),
    std::string("^z.z.z.z.z.z.z.z.z.z.z.z.z.z*$"),
    std::string("^[z][z][z][z][z][z][z][z][z][z][z][z][z][z][z]\\S*$"),
    std::string("^[az]\\S\\D*$"),
};

std::vector<std::tuple<hs_database_t*, hs_scratch_t*>> regexps;

const std::vector<std::string> chunks = {
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "10.10.10.10 cjdhjhsdclkjhasl dflaskijd flkzsjd vlkszJ cvlsJKHD CVlaskjdvcl sdjvl ksDJv lkj lkj lzkjsdf lkj lzskdjv lkzj  66678",
    "hello world !",
    "bar!234ahem.. 'hello world !' ..c !hello worldzzz !zzzzzzzzzzzzzzzzzzz ksajf 874r hbsdfk i7r kjasdhf ikasuwhfia7234 kwaejhfkawehf7234h zzzzzzzzzzzzzzzzzzzzzzzzz dsssssssssssssssssssssssssssssssssssssssss aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ssssssssssssssssssssssssssssssssssssssss ddddddddddddddddddddddddddddddddddddddddddddddddd ffffffffffffffffffffffffffffffffffffffffffff ggggggggggggggggggggggggggggggggggggggggggggggggggg hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk llllllllllllllllllllllllllllllllllllllllllllllllllll qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr ttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppiauwdhfl,asdnfliehjrsgoirtjoersahjrouh waei7yi7q34f kwejfg hello world",
    "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",
};

int main(int argc, char *argv[])
{
    regexps.resize(rules.size());

    for (size_t i = 0; i < rules.size(); i++)
    {
        hs_compile_error_t *compile_err;
        hs_database_t *db;
        hs_scratch_t *scratch;

        hs_error_t err = hs_compile(rules[i].c_str(), HS_FLAG_DOTALL | HS_FLAG_SINGLEMATCH, HS_MODE_BLOCK, NULL, &db, &compile_err);
        if (err != HS_SUCCESS)
        {
            std::cerr << "ERROR: Unable to compile pattern \"" << rules[i] << "\": " << compile_err->message << std::endl;
            hs_free_compile_error(compile_err);
            return -1;
        }

        err = hs_alloc_scratch(db, &scratch);
        if (err != HS_SUCCESS)
        {
            std::cerr << "ERROR: Unable to allocate scratch space. Exiting." << std::endl;
            hs_free_database(db);
            return -1;
        }

        regexps[i] = std::make_tuple(db, scratch);
    }

    const auto start_time = std::chrono::high_resolution_clock::now();

    for (size_t i = 0; i < N_REGEX_ITERATIONS; i++)
    {
        for (const auto &re : regexps)
        {
            for (size_t j = 0; j < N_CHUNKS_ITERATIONS; j++)
            {
                for (auto chunk : chunks)
                {
                    hs_error_t err = hs_scan(static_cast<hs_database_t*>(std::get<0>(re)), chunk.c_str(), chunk.size(), 0, static_cast<hs_scratch_t*>(std::get<1>(re)), [](unsigned int id, unsigned long long from, unsigned long long to, unsigned int flags, void *ctx) -> int {
                        return 0;
                    }, nullptr);
                    if (err != HS_SUCCESS)
                    {
                        std::cerr << "ERROR: Unable to scan chunk. Exiting." << std::endl;
                        return -1;
                    }
                }
            }
        }
    }

    const auto end_time = std::chrono::high_resolution_clock::now();
    const auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time).count();

    std::cout << "Execution time: " << duration << "ms" << std::endl;

    return 0;
}