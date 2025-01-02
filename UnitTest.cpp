#include <iostream>
#include "Solution.hpp"

struct testcase {
    vector<string> words;
    vector<vector<int>> queries;
    vector<int> outputs;
};

class UnitTest {
private:
    vector<testcase> testcases;
    Solution obj;
public:
    UnitTest() {
        testcases = {
            {{"aba","bcb","ece","aa","e"}, {{0,2},{0,4},{1,1}}, {2,3,0}},
            {{"a","e","i"}, {{0,2},{0,1},{2,2}}, {3,2,1}}
        };
    }

    void test() {
        for(int i = 0; i < testcases.size(); ++i) {
            vector<string> words = testcases[i].words;
            vector<vector<int>> queries = testcases[i].queries;
            vector<int> outputs = testcases[i].outputs;

            vector<int> results = obj.vowelStrings(words, queries);
            bool pass = true;
            if(results.size() == outputs.size()) {
            for(int j = 0; j < results.size(); ++j)
                if(results[i] != outputs[i]) { pass = false; break; }
            }
            else pass = false;

            cout << "TestCase " << i+1 << ": " << (pass ? "passed" : "failed") << endl;
        }
    }
};

int main() {
    UnitTest test;
    test.test();
}