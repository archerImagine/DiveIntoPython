import example12

def output(data, format='text'):
	output_function = getattr(example12,'output_%s' %format, example12.output_text)
	return output_function()

if __name__ == '__main__':	
	format = str(raw_input("Enter the output format: "))
	output("hello", format)