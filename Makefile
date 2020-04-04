prepare:
	brew install wget

init:
	mkdir datasets
	wget http://nlp.cs.aueb.gr/software_and_datasets/Enron-Spam/preprocessed/enron1.tar.gz -P datasets
	tar -zxvf datasets/enron1.tar.gz -C datasets/
	rm -r datasets/enron1.tar.gz
