#ifndef PROGRESSTRACKER_H
#define PROGRESSTRACKER_H

#include <iomanip>
#include <locale>
#include <string>
#include <ctime>

template<class T>
std::string FormatWithCommas(T value)
{
    std::stringstream ss;
    ss.imbue(std::locale(""));
    ss << std::fixed << value;
    return ss.str();
}

class ProgressTracker
{
    public:
    ProgressTracker(const std::string &title, uint64_t length, int stagger)
    :title_(title), length_(length), stagger(stagger)
    {
        time(&start_);
    }

    int timer()
    {
        time(&end_);
        return end_ - start_;
    }

    void update(const uint64_t iteration)
    {
        time(&end_);
        elapsed = end_ - start_;

        hour = elapsed / 3600;
        elapsed %= 3600;
        min = elapsed / 60;
        second = elapsed % 60;

        output = FormatWithCommas(iteration);

        std::ostringstream stringStream;
        stringStream << "\033[" << stagger + 9 << ";0H"
                     << title_ << " " << stagger << ": " 
                     << "Processed: " << output
                     << std::setprecision(3)<< std::setfill('0') << std::fixed
                     << " ( "
                     << std::setw(5) << iteration / double(length_) * 100 << "% )"
                     << " Time: " << std::setw(2) << hour << "h "
                     << std::setw(2) << min << "m "
                     << std::setw(2) << second << "s";
        output = stringStream.str();
        int len = output.size();
        erase = std::string(len, '\b');

        std::cout << erase << output << std::endl;
    }

    private:
    const std::string title_;
    const uint64_t length_;
    int stagger;

    time_t start_;
    time_t end_;
    time_t elapsed;

    int hour, min, second;

    std::string output;
    std::string erase;
    


};

#endif