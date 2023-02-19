package starter;

import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

// complete the test and dataprovider method

public class DefectTest {
    @Test(dataProvider = "")
    public void isValidReturnsFalseForInvalidDefects(String name, String summary, String details) {
        
    }

    @DataProvider(name = "")
    public Object[][] invalidDefectData() {
        // read from your spreadsheet
        // return a 2D array of inputs and expected urls
    }
}
