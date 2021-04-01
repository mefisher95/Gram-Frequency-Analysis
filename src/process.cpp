#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <sys/stat.h>

#include "bit_grams.h"
#include "ProgressTracker.h"

void write_one_gram(std::map< uint32_t, uint64_t> &m, int process)
{
    std::ofstream file("./grams/onegram-" + std::to_string(process) + ".txt", std::ios_base::out);
    for(auto elem : m) 
    {
        file << char(elem.first) << ' ' << elem.second << '\n';
    }
    file.close();
}

void write_two_gram(std::map< uint32_t, uint64_t> &m, int process)
{
    std::ofstream file("./grams/twogram-" + std::to_string(process) + ".txt", std::ios::out | std::ios::trunc);

    for(auto elem : m) 
    {
        uint32_t element = elem.first;
        int one = char(element >> 8); 
        int two = char(element);

        std::string output(std::string(1, char(one)) + 
                           std::string(1, char(two)) + " " + 
                           std::to_string(elem.second));

        file << output << std::endl;
    }
}

void write_three_gram(std::map< uint32_t, uint64_t> &m, int process)
{
    std::ofstream file("./grams/threegram-" + std::to_string(process) + ".txt", std::ios::out | std::ios::trunc);

    for(auto elem : m) 
    {
        uint32_t element = elem.first;
        int one = char(element >> 16); 
        int two = char(element >> 8);
        int three = char(element);

        std::string output(std::string(1, char(one)) + 
                           std::string(1, char(two)) + 
                           std::string(1, char(three)) + " " + 
                           std::to_string(elem.second));

        file << output << std::endl;
    }
}

void write_four_gram(std::map< uint32_t, uint64_t> &m, int process)
{
    std::ofstream file("./grams/fourgram-" + std::to_string(process) + ".txt", std::ios::out | std::ios::trunc);

    for(auto elem : m) 
    {
        uint32_t element = elem.first;
        int one = char(element >> 24); 
        int two = char(element >> 16);
        int three = char(element >> 8);
        int four = char(element);

        std::string output(std::string(1, char(one)) + 
                           std::string(1, char(two)) + 
                           std::string(1, char(three)) + 
                           std::string(1, char(four)) + " " + 
                           std::to_string(elem.second));
        
        file << output << std::endl;
    }
}

int main(int argc, char** argv)
{
    std::ifstream master;
    master.open(argv[3], std::ios::app); // complete filepath

    struct stat filestatus;
    stat( "master.txt", &filestatus );

    float batchsize = filestatus.st_size;
    int process = 0;


    process = strtol(argv[1], NULL, 10);
    batchsize = strtol(argv[2], NULL, 10);
    master.seekg(process * batchsize);


    // input variables
    char x;
    u_int32_t bitlist = 0;
    uint64_t amount = 0;

    // time_t begin, end;
    // time(&begin);

    ProgressTracker tracker("Worker", batchsize, process);

    while (!master.eof() && batchsize > amount)
    {
        if (amount % 1000000 == 0 && amount > 1)
        {

            tracker.update(amount);
        } 
        master >> x;

        insert_letter(bitlist, x);
        int one = one_gram(bitlist);
        int two = two_gram(bitlist);
        int three = three_gram(bitlist);
        int four = four_gram(bitlist);

        ++amount;
        ++ONE_GRAM[one];
        if (amount > 1) ++TWO_GRAM[two];
        if (amount > 2) ++THREE_GRAM[three];
        if (amount > 3) ++FOUR_GRAM[four];
    }
    std::cout << std::endl;

    write_one_gram(ONE_GRAM, process);
    write_two_gram(TWO_GRAM, process);
    write_three_gram(THREE_GRAM, process);
    write_four_gram(FOUR_GRAM, process);    
    
    return 0;
}