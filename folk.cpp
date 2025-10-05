#include <iostream>
#include <vector>
#include <algorithm>
#include <cctype>
#include <string>
using namespace std;

string slicer(string media_name, int start)
{
    size_t pos = media_name.substr(start, media_name.size() - start).find_last_of("0123456789") + start; // 9
    if (pos == string::npos)
        return "";
    size_t begin = media_name.find_last_not_of("0123456789");
    return media_name.substr(begin + 1, pos - begin);
}

void put(vector<pair<string, string>>)
{
}
int main()
{
    int n, location;
    string tmp_str;
    vector<pair<string, string>> movies;
    vector<pair<int, string>> shows;
    pair<string, string> tmp_movie;
    pair<int, string> tmp_show;
    cin >> n;
    for (size_t i = 0; i < n; i++)
    {
        cin >> tmp_str;

        if (i == 0)
        {
            location = tmp_str.find("-") + 1;
            if (slicer(tmp_str, location) == "")
            {
                tmp_movie.first = tmp_str.substr(0, location);
                tmp_movie.second = tmp_str.substr(location, tmp_str.size() - location);
                movies.push_back(tmp_movie);
                continue;
            }
            tmp_show.first = stoi(slicer(tmp_str, location));
            tmp_show.second = tmp_str.substr(0, tmp_str.size() - slicer(tmp_str, location).size());
            shows.push_back(tmp_show);
            continue;
        }
        if (slicer(tmp_str, location) == "")
        {
            tmp_movie.first = tmp_str.substr(0, location);
            tmp_movie.second = tmp_str.substr(location, tmp_str.size() - location);
            movies.push_back(tmp_movie);
            continue;
        }
        tmp_show.first = stoi(slicer(tmp_str, location));
        tmp_show.second = tmp_str.substr(0, tmp_str.size() - slicer(tmp_str, location).size());
        shows.push_back(tmp_show);
    }
    sort(movies.begin(), movies.end());
    sort(shows.begin(), shows.end());
    cout << "\nThe output:" << endl;
    for (pair<string, string> x : movies)
        cout << x.first << x.second << endl;
    for (pair<int, string> x : shows)
        cout << x.second << x.first << endl;
}

/*
5
1-ironman1
2-ironman2
1-ironman2
2-ironman1
5-antman


1-ironman500
2-ironman75
1-ironman2
5-antman
5-batman

1-ironman500
1-ironman75
1-ironman2
*/