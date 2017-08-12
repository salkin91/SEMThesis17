# SEMThesis17
This is our bachelor thesis at the Software Engineering and Management program at University of Gothenburg 2017

## How to run the experiment
* Download UPPAAL with the SMC extension
* Open model/dsu_system.xml in UPPAAL
* To declare how many components to be tested on - go to **Declaraitions** and change **const int components** to the number of components to be tested
* To select which method to test - go to **System declarations** and select which **system variables** to use
* Go to **Verifier** select **simulate 2000 [ <= 1000] {Manager.Done}** in the list and then press **Check**
* When property been satisfied right click **simulate 2000 [ <= 1000] {Manager.Done}** and click on the popup
* Right click the graph and export as Comma Seperated Values

## How to use code/uppaalPlotSplitter.py
* Download and set up Python
* The first argument of **uppaalPlotSplitter.py is the extracted File from UPPAAl and the second argument is the new .csv file that will be generated with fixed data to be used in the statistical test.
* Example:
```python
python uppaalPlotSpliter.py extractedFile.csv newGeneratedFile.csv
```

## How to set up the data in RStudio
* Import CSV
  * Delimiter - Whitespace
  * Comment - #

* Remove bad values
  * dataName = subset(dataName,done!=0)
  * dataName = subset(dataName,time<1000)

* Remove duplicates
  * dataNamn = unique(dataName)
