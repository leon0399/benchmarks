#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <time.h>

#define UPPER_BOUND 5000000
#define PREFIX 32338

// -----------------------------
// Struct definitions
// -----------------------------

typedef struct Node {
    struct ChildMap *children;
    int num_children;
    bool terminal;
} Node;

typedef struct ChildMap {
    char key;
    struct Node *value;
} ChildMap;

typedef struct {
    int limit;
    bool *prime;
} Sieve;

// -----------------------------
// Function declarations
// -----------------------------
Sieve* Sieve_new(int limit);
void Sieve_free(Sieve *self);
Sieve* Sieve_calc(Sieve *self);
Sieve* Sieve_omit_squares(Sieve *self);
void step1(Sieve *self, int x, int y);
void step2(Sieve *self, int x, int y);
void step3(Sieve *self, int x, int y);
void loop_y(Sieve *self, int x);
void loop_x(Sieve *self);
int* to_list(Sieve *self, int *out_size);

Node* Node_new();
void Node_free(Node *node);
Node* generate_tree(int *list, int size);
Node* Node_get_child(Node *node, char ch);
Node* Node_add_child(Node *node, char ch);

int* find(int upper_bound, int prefix, int *out_size);
char* to_string(int *arr, int size);

// -----------------------------
// Sieve Implementation
// -----------------------------

Sieve* Sieve_new(int limit) {
    Sieve *self = malloc(sizeof(Sieve));
    self->limit = limit;
    self->prime = calloc(limit + 1, sizeof(bool));
    return self;
}

void Sieve_free(Sieve *self) {
    if (!self) return;
    free(self->prime);
    free(self);
}

Sieve* Sieve_omit_squares(Sieve *self) {
    for (int r = 5; r * r < self->limit; ++r) {
        if (self->prime[r]) {
            for (int i = r * r; i < self->limit; i += r * r) {
                self->prime[i] = false;
            }
        }
    }
    return self;
}

void step1(Sieve *self, int x, int y) {
    int n = (4 * x * x) + (y * y);
    if (n <= self->limit && (n % 12 == 1 || n % 12 == 5)) {
        self->prime[n] = !self->prime[n];
    }
}

void step2(Sieve *self, int x, int y) {
    int n = (3 * x * x) + (y * y);
    if (n <= self->limit && n % 12 == 7) {
        self->prime[n] = !self->prime[n];
    }
}

void step3(Sieve *self, int x, int y) {
    int n = (3 * x * x) - (y * y);
    if (x > y && n <= self->limit && n % 12 == 11) {
        self->prime[n] = !self->prime[n];
    }
}

void loop_y(Sieve *self, int x) {
    for (int y = 1; y * y < self->limit; ++y) {
        step1(self, x, y);
        step2(self, x, y);
        step3(self, x, y);
    }
}

void loop_x(Sieve *self) {
    for (int x = 1; x * x < self->limit; ++x) {
        loop_y(self, x);
    }
}

Sieve* Sieve_calc(Sieve *self) {
    loop_x(self);
    return Sieve_omit_squares(self);
}

int* to_list(Sieve *self, int *out_size) {
    int *result = malloc((self->limit + 1) * sizeof(int));
    int idx = 0;
    result[idx++] = 2;
    result[idx++] = 3;
    for (int p = 5; p <= self->limit; ++p) {
        if (self->prime[p]) {
            result[idx++] = p;
        }
    }
    *out_size = idx;
    return result;
}

// -----------------------------
// Trie Tree (Node) Implementation
// -----------------------------

Node* Node_new() {
    Node *node = malloc(sizeof(Node));
    node->children = NULL;
    node->num_children = 0;
    node->terminal = false;
    return node;
}

Node* Node_get_child(Node *node, char ch) {
    for (int i = 0; i < node->num_children; ++i) {
        if (node->children[i].key == ch) {
            return node->children[i].value;
        }
    }
    return NULL;
}

Node* Node_add_child(Node *node, char ch) {
    node->children = realloc(node->children, (node->num_children + 1) * sizeof(ChildMap));
    node->children[node->num_children].key = ch;
    node->children[node->num_children].value = Node_new();
    node->num_children++;
    return node->children[node->num_children - 1].value;
}

void Node_free(Node *node) {
    if (!node) return;
    for (int i = 0; i < node->num_children; ++i) {
        Node_free(node->children[i].value);
    }
    free(node->children);
    free(node);
}

Node* generate_tree(int *list, int size) {
    Node *root = Node_new();
    char buffer[32];
    for (int i = 0; i < size; ++i) {
        snprintf(buffer, sizeof(buffer), "%d", list[i]);
        Node *head = root;
        for (int j = 0; j < strlen(buffer); ++j) {
            Node *child = Node_get_child(head, buffer[j]);
            if (!child) {
                child = Node_add_child(head, buffer[j]);
            }
            head = child;
        }
        head->terminal = true;
    }
    return root;
}

// -----------------------------
// BFS Find Function
// -----------------------------

typedef struct QueueNode {
    Node *node;
    char *prefix;
    struct QueueNode *next;
} QueueNode;

void enqueue(QueueNode **front, QueueNode **rear, Node *node, const char *prefix) {
    QueueNode *new_node = malloc(sizeof(QueueNode));
    new_node->node = node;
    new_node->prefix = strdup(prefix);
    new_node->next = NULL;
    if (*rear) (*rear)->next = new_node;
    else *front = new_node;
    *rear = new_node;
}

QueueNode* dequeue(QueueNode **front, QueueNode **rear) {
    if (!*front) return NULL;
    QueueNode *temp = *front;
    *front = (*front)->next;
    if (!*front) *rear = NULL;
    return temp;
}

int* find(int upper_bound, int prefix, int *out_size) {
    Sieve *s = Sieve_new(upper_bound);
    Sieve_calc(s);
    int prime_count;
    int *primes = to_list(s, &prime_count);

    char str_prefix[32];
    snprintf(str_prefix, sizeof(str_prefix), "%d", prefix);

    Node *head = generate_tree(primes, prime_count);
    for (int i = 0; i < strlen(str_prefix); ++i) {
        head = Node_get_child(head, str_prefix[i]);
        if (!head) {
            *out_size = 0;
            free(primes);
            Sieve_free(s);
            return NULL;
        }
    }

    QueueNode *front = NULL, *rear = NULL;
    enqueue(&front, &rear, head, str_prefix);

    int *result = malloc(1024 * sizeof(int));
    int count = 0, capacity = 1024;

    while (front) {
        QueueNode *q = dequeue(&front, &rear);
        Node *node = q->node;

        if (node->terminal) {
            if (count >= capacity) {
                capacity *= 2;
                result = realloc(result, capacity * sizeof(int));
            }
            result[count++] = atoi(q->prefix);
        }

        for (int i = 0; i < node->num_children; ++i) {
            char new_prefix[64];
            snprintf(new_prefix, sizeof(new_prefix), "%s%c", q->prefix, node->children[i].key);
            enqueue(&front, &rear, node->children[i].value, new_prefix);
        }

        free(q->prefix);
        free(q);
    }

    *out_size = count;

    Node_free(head);
    free(primes);
    Sieve_free(s);

    return result;
}

// -----------------------------
// Utility Functions
// -----------------------------

char* to_string(int *arr, int size) {
    char *buf = malloc(size * 12);
    buf[0] = '\0';
    strcat(buf, "[");
    for (int i = 0; i < size; ++i) {
        char num[16];
        sprintf(num, "%d", arr[i]);
        strcat(buf, num);
        if (i < size - 1) strcat(buf, ", ");
    }
    strcat(buf, "]");
    return buf;
}

// -----------------------------
// Main Function
// -----------------------------

int main() {
    clock_t start_time = clock();

    int result_size;
    int *result = find(UPPER_BOUND, PREFIX, &result_size);

    char *result_str = to_string(result, result_size);
    printf("%s\n", result_str);

    clock_t end_time = clock();
    double duration = ((double)(end_time - start_time) / CLOCKS_PER_SEC) * 1000.0;
    printf("Execution time: %.2fms\n", duration);

    free(result);
    free(result_str);
    return 0;
}
