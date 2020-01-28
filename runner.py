import subprocess
import sys
import os

class Runner:
	def runner(spec_file, output_dir, module_name):
		subprocess.call('python3 {}/swagger_django_generator/generator.py {} --output-dir {} --module-name {}'
			.format(os.path.dirname(os.path.realpath(__file__)), spec_file, output_dir, module_name), shell=True)

