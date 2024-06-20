#include <iostream>
#include <string>
#include <chrono>
#include <vector>
#include <regex>
#include <fstream>
#include <filesystem>

const size_t N_REGEX_ITERATIONS = 1000;
const size_t N_CHUNKS_ITERATIONS = 10;

// array of regexs
const std::vector<std::regex> regexps = {
    std::regex("[Hh]ello [Ww]orld[!]?"),
    std::regex("[Hh]ello [Ww]orld[!]?$"),
    std::regex("[0-9][0-9][0-9][0-9][0-9]"),
    std::regex("[0-9][0-9][0-9][0-9][0-9]$"),
    std::regex("[CV]V[a-z]askjdvc[a-z0-9A-Z]"),
    std::regex("^[0-9][0-9]\\.[0-9][0-9]\\.[0-9][0-9]\\.[0-9][0-9]\\s[a-zA-Z]"),
    std::regex("^z.*$"),
    std::regex("^z.z.z.z.z.z.z.z.z.z.z.z.z.z*$"),
    std::regex("^[z][z][z][z][z][z][z][z][z][z][z][z][z][z][z]\\S*$"),
    std::regex("^[az]\\S\\D*$"),
};

const std::vector<std::string> chunks = {
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "10.10.10.10 cjdhjhsdclkjhasl dflaskijd flkzsjd vlkszJ cvlsJKHD CVlaskjdvcl sdjvl ksDJv lkj lkj lzkjsdf lkj lzskdjv lkzj  66678",
    "hello world !",
    "bar!234ahem.. 'hello world !' ..c !hello worldzzz !zzzzzzzzzzzzzzzzzzz ksajf 874r hbsdfk i7r kjasdhf ikasuwhfia7234 kwaejhfkawehf7234h zzzzzzzzzzzzzzzzzzzzzzzzz dsssssssssssssssssssssssssssssssssssssssss aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ssssssssssssssssssssssssssssssssssssssss ddddddddddddddddddddddddddddddddddddddddddddddddd ffffffffffffffffffffffffffffffffffffffffffff ggggggggggggggggggggggggggggggggggggggggggggggggggg hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk llllllllllllllllllllllllllllllllllllllllllllllllllll qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr ttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppiauwdhfl,asdnfliehjrsgoirtjoersahjrouh waei7yi7q34f kwejfg hello world",
    "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",
};

int main(int argc, char *argv[])
{
    const auto start_time = std::chrono::high_resolution_clock::now();

    for (size_t i = 0; i < N_REGEX_ITERATIONS; i++)
    {
        for (const auto &re : regexps)
        {
            for (size_t j = 0; j < N_CHUNKS_ITERATIONS; j++)
            {
                for (auto chunk : chunks)
                {
                    for (std::smatch sm; std::regex_search(chunk, sm, re);)
                    {
                        // std::cout << sm.str() << std::endl;
                        chunk = sm.suffix().str();
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