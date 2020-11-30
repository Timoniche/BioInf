//
// Created by Dmitrii Dulaev on 28.11.2020.
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

typedef long double ld;

vector<pair<ld, ld>> input;
vector<ld> tmp1;
vector<ld> tmp2;

int N;

void read_input() {

    N = 1000;

    const char *f1 = "dist_from_if_theory.txt";
    const char *f2 = "dist_mat_practice.txt";

    freopen(f1, "r", stdin);
    for (int i = 0; i < N * N; i++) {
        ld x1;
        cin >> x1;
        tmp1.push_back(x1);
    }

    freopen(f2, "r", stdin);
    for (int i = 0; i < N * N; i++) {
        ld x2;
        cin >> x2;
        tmp2.push_back(x2);
    }

    for (int i = 0; i < N * N; ++i) {
        input.emplace_back(tmp1[i], tmp2[i]);
    }
}

int main() {
    read_input();
    pair<ld, ld> sums;
    cout.precision(7);
    for_each(input.begin(), input.end(), [&](pair<ld, ld> &p) {
        sums.first += p.first;
        sums.second += p.second;
    });
    // cout << sums.first << " " << sums.second << endl;
    pair<ld, ld> avgs;
    avgs.first = ld(sums.first) / N;
    avgs.second = ld(sums.second) / N;
    // cout << avgs.first << " " << avgs.second << endl;
    ld nom = 0.0;
    ld dx2_sum = 0.0;
    ld dy2_sum = 0.0;
    for (int i = 0; i < N; ++i) {
        ld dx = input[i].first - avgs.first;
        ld dy = input[i].second - avgs.second;
        nom += dx * dy;

        dx2_sum += dx * dx;
        dy2_sum += dy * dy;
    }

    ld pearson;
    ld denom = sqrt(dx2_sum) * sqrt(dy2_sum);
    denom == 0 ? pearson = 0.0 : pearson = nom / denom;
    cout << setprecision(7) << pearson;
    return 0;
}