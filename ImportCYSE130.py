#include "Assignment.h"
#include "Course.h"
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <iomanip>
#include <stdlib.h>
#include <stdio.h>
#include <fstream>
#include <sstream>

using namespace std;

/* input.txt
CSCI-110, 101
4
Assignment 1, 10/1/2015
Assignment 2, 10/2/2015
Assignment 3, 10/3/2015
Assignment 4, 10/4/2015
CSCI-112, 102
3
Assignment 1, 10/1/2015
Assignment 2, 10/2/2015
Assignment 3, 10/3/2015
CSCI-113, 103
2
Assignment 1, 10/1/2015
Assignment 2, 10/2/2015
*/

int main(){
    //read in file
    ifstream inputFile;
    inputFile.open("input.txt");
    if(!inputFile){
        cout << "Error opening file" << endl;
        return 1;
    }
    //read line by line
    string line;
    vector<Course> courses;
    while(getline(inputFile, line)){
        //split line by comma
        stringstream ss(line);
        string token;
        vector<string> tokens;
        while(getline(ss, token, ',')){
            tokens.push_back(token);
        }
        //create course
        Course course(tokens[0].c_str(), atoi(tokens[1].c_str()));
        //read next line
        getline(inputFile, line);
        //convert to int
        int numAssignments = atoi(line.c_str());
        for(int i = 0; i<numAssignments; i++){
            //read next line
            getline(inputFile, line);
            //split line by comma
            stringstream ss2(line);
            string token2;
            vector<string> tokens2;
            while(getline(ss2, token2, ',')){
                tokens2.push_back(token2);
            }
            //create assignment
            char *name = new char[tokens2[0].length() + 1];
            strcpy(name, tokens2[0].c_str());
            Assignment assignment(name, tokens2[1].c_str());
            //add assignment to course
            course.addAssignment(assignment);
        }
        courses.push_back(course); 
    } 
    //display courses
    cout << setw(20) << left << "Course_Name" << setw(10) << left << "Number" << endl;
    cout << courses.size(); 
    for(int i = 0; i < courses.size(); i++){
        courses[i].display();
    }
    return 0; 
}