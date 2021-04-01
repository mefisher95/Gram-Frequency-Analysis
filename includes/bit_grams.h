#ifndef BITGRAM_H
#define BITGRAM_H

#include <vector>
#include <map>

std::map< uint32_t, uint64_t > generate_one_gram();
std::map< uint32_t, uint64_t > generate_two_gram();
std::map< uint32_t, uint64_t > generate_three_gram();
std::map< uint32_t, uint64_t > generate_four_gram();

std::map < uint32_t, uint64_t > ONE_GRAM = generate_one_gram();
std::map < uint32_t, uint64_t > TWO_GRAM = generate_two_gram();
std::map < uint32_t, uint64_t > THREE_GRAM = generate_three_gram();
std::map < uint32_t, uint64_t > FOUR_GRAM = generate_four_gram();

void print_bits(uint32_t string)
{
    for (int i = 0; i < 32; ++i)
    {
        if (i % 8 == 0 && i > 0) std::cout << ' ';
        std::cout << string % 2;
        string >>= 1;
    }
    std::cout << std::endl;
}

int one_gram(uint32_t string)
{
    string <<= 24;
    string >>= 24;

    return string;
}

int two_gram(uint32_t string)
{
    string <<= 16;
    string >>= 16;

    return string;
}

int three_gram(uint32_t string)
{
    string <<= 8;
    string >>= 8;

    return string;
}

int four_gram(uint32_t string)
{
    return string;
}

void insert_letter(uint32_t &string, char a)
{
    string <<= 8;
    string |= a;
}

std::map< uint32_t, uint64_t > generate_one_gram()
{
    // std::vector< uint32_t > list;
    std::map< uint32_t, uint64_t > list;
    uint32_t combo = 0;

    for (char c = 'a'; c < 'a' + 26; ++c)
    {
        combo = 0;
        insert_letter(combo, c);
        list.insert({ combo, uint64_t(0)});
    }
    return list;
}

std::map< uint32_t, uint64_t > generate_two_gram()
{
    std::map< uint32_t, uint64_t > list;

    uint32_t combo = 0;

    for (char c = 'a'; c < 'a' + 26; ++c)
    {
        for (char d = 'a'; d < 'a' + 26; ++d)
        {
            combo = 0;
            insert_letter(combo, c);
            insert_letter(combo, d);
            list.insert({combo, uint64_t(0)});

        }    
    }

    return list;
}

std::map< uint32_t, uint64_t > generate_three_gram()
{
    std::map< uint32_t, uint64_t > list;

    uint32_t combo = 0;

    for (char c = 'a'; c < 'a' + 26; ++c)
    {
        for (char d = 'a'; d < 'a' + 26; ++d)
        {
            for (char e = 'a'; e < 'a' + 26; ++e)
            {
                combo = 0;
                insert_letter(combo, c);
                insert_letter(combo, d);
                insert_letter(combo, e);
                list.insert({combo, 0});
            }
        }    
    }
    return list;
}

std::map< uint32_t, uint64_t > generate_four_gram()
{
    uint32_t combo = 0;
    std::map< uint32_t, uint64_t > list;

    for (char c = 'a'; c < 'a' + 26; ++c)
    {
        for (char d = 'a'; d < 'a' + 26; ++d)
        {
            for (char e = 'a'; e < 'a' + 26; ++e)
            {
                for (char f = 'a'; f < 'a' + 26; ++f)
                {
                    combo = 0;
                    insert_letter(combo, c);
                    insert_letter(combo, d);
                    insert_letter(combo, e);
                    insert_letter(combo, f);
                    list.insert({combo, uint64_t(0)});
                }
            }
        }    
    }
    return list;
}

#endif