# Save_A_Copy_Batch
This script is a batch processing tool for copying MXDs into a format that can be used by older versions of ArcMap.

### Directions
1. Add ```SaveACopyBatch.py``` to your desired directory.

2. In the command line terminal  make your way to that directory using the ```cd ``` command.

3. Run the following command :
 ```
 C:\Python27\ArcGIS10.4\python.exe SaveACopyBatch.py
 ```

4. First you will be prompted to define what previous version(s) of ArcMap you want your mxd to exported as. The following values are excepted individually or as a group:

  ```python
    #Possible Values
    10.3, 10.1, 10.0, 9.3, 9.2, 9.0, and 8.3

    # Entering  a Single Values
    10.0

    #Entering multiple values
    10.1 10.0
  ```

5. Next you will be asked to provide the directory of the folder containing your mxds. You can manually type this in or drag the folder in the terminal. Then hit enter.

6. When the script is completed sucessfully you will have a folder(s) containing the version specific mxd in the directory containing ```SaveACopyBatch.py```.
