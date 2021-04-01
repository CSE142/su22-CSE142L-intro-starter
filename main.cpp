#include "archlab.hpp"
#include <stdlib.h>
#include <getopt.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

// lab.py doesn't specify this an input, so changes won't propogate to the autograder.

// The student's code.cpp should provide this function.
void greet(const std::string & salutation, const std::string & name);

int main(int argc, char *argv[]) {
  
	std::string name;
	archlab_add_option<std::string>("name", name , "Ada",  "Your name");
	archlab_parse_cmd_line(&argc, argv);

	std::string salutation((std::getenv("SALUTATION") && std::string("") != std::getenv("SALUTATION")) ? std::getenv("SALUTATION") : "Howdy");
	
	{
		ArchLabTimer timer;
		timer.go();
		greet(salutation, name);
	}
	archlab_write_stats();
	
	return 0;
}	

