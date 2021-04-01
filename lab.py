# Students should not edit this file, since changes here will _only_
# affect how your code runs locally.  It will not change how your code
# executes in the cloud.
from ArchLab.CSE141Lab import CSE141Lab, test_configs
import unittest
from gradescope_utils.autograder_utils.decorators import weight
import ArchLab.Runner as Runner
import os
import json
import logging as log
import parameterized


class ThisLab(CSE141Lab):
    def __init__(self, **kwargs):
        super(ThisLab, self).__init__(
            lab_name = "Introduction to the Development Environment",
            short_name = "intro",
            # These are the files runlab will collect from the
            # student's repo.  shell-style globs are allowed (e.g.,
            # '*.cpp').
            input_files = ['code.cpp', 'config.env', 'outputs/*'],
            # These are the outputs runlab will collect.
            output_files = ['code.out', 'code-stats.csv'],
            # This is the command that will be run for the lab.
            default_cmd = ['make'],
            # This is the repo to run the lab in.  This should be the starter repo provided to the student.
            repo = kwargs.get("repo") or "https://github.com/NVSL/CSE141pp-Lab-Introduction-to-the-Development-Environment",
            # The tag to use in that repo.
            reference_tag = kwargs.get("reference_tag") or "master",
            # These are environment variables student is allowed to set in config.env.
            valid_options={"salutation": 'short|long|formal',
                           "EXTRA_OPTIONS": "<cmdline options for code.exe>"
            }
        )


    # The MetaRegressions test are for the lab structure itself.
    # These should ensure that the lab creates the correct files and
    # that the scoring works as expected.  
    class MetaRegressions(CSE141Lab.MetaRegressions):
        @parameterized.parameterized.expand(test_configs("solution", "."))
        def test_solution(self, solution, flags):
            result, tag = self.run_solution(solution, flags)
            
            self.assertFileExists("code.out",tag=tag)
            self.assertFileExists("code-stats.csv",tag=tag)
            if not flags.devel:
                self.assertRegex(self.read_file("code-stats.csv", root="."), "inst_count",  f"Failed on {tag}: looking for 'inst_count' in code-stats.csv")
            else:
                self.assertRegex(self.read_file("code-stats.csv", root="."), 'runtime', f"Failed on {tag}: looking for 'runtime' in code-stats.csv")
                
            js = result.results

            if solution == ".":
                if flags.grades_valid():
                    self.assertEqual(float(js['gradescope_test_output']['score']), 3, f"Failed on {tag}: score check")
            elif solution == "solution":
                if flags.grades_valid():
                    self.assertEqual(float(js['gradescope_test_output']['score']), 7, f"Failed on {tag}: score check")
