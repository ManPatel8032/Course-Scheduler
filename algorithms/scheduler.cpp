#include <bits/stdc++.h>
#include "json.hpp"  // include nlohmann/json library

using json = nlohmann::json;
using namespace std;

// Function to perform topological sort
vector<string> topoSort(map<string, vector<string>>& graph, map<string, int>& indegree) {
    queue<string> q;
    vector<string> order;

    for (auto& pair : indegree)
        if (pair.second == 0)
            q.push(pair.first);

    while (!q.empty()) {
        string course = q.front();
        q.pop();
        order.push_back(course);

        for (auto& neighbor : graph[course]) {
            indegree[neighbor]--;
            if (indegree[neighbor] == 0)
                q.push(neighbor);
        }
    }

    if (order.size() != indegree.size()) {
        cerr << "Error: Circular dependency detected!" << endl;
    }

    return order;
}

int main() {
    // Read input JSON
    ifstream inFile("input_courses.json");
    json input;
    inFile >> input;

    map<string, vector<string>> graph;
    map<string, int> indegree;

    // Build graph
    for (auto& course : input["courses"]) {
        string code = course["code"];
        indegree[code]; // initialize

        for (auto& pre : course["prerequisites"]) {
            graph[pre].push_back(code);
            indegree[code]++;
        }
    }

    // Get sorted order
    vector<string> result = topoSort(graph, indegree);

    // Write output JSON
    json output;
    output["order"] = result;

    ofstream outFile("output_order.json");
    outFile << output.dump(4);
    outFile.close();

    cout << "Course order generated successfully!\n";
    return 0;
}
