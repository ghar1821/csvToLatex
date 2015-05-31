def csvToLatex(csvFile):
	csv = open(csvFile,'r')
	line = csv.readline().replace('_','\\_').split(',')
	latex = '\\begin{table}[h]\n\\begin{tabular}{'
	for x in xrange(0,len(line)):
		latex += '|l'
	latex += '|}\n' + '\hline\n'
	for x in xrange(0,len(line)):
		if x == len(line) - 1:
			latex += line[x].strip() + ' \\\\' + ' \hline\n'
		else:
			latex += line[x].strip() + ' & '
	for line in csv:
		row = line.replace('_','\\_').split(',')
		for x in xrange(0,len(row)):
			if x == len(row) - 1:
				latex += row[x].strip() + ' \\\\' + ' \hline\n'
			else:
				latex += row[x].strip() + ' & '
	latex += '\end{tabular}\n\end{table}'
	print latex
	csv.close()

csv_file = raw_input('Enter CSV file absolute location: ')
csvToLatex(csv_file)
