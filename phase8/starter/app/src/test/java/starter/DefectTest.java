package starter;

import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

// complete the test and dataprovider method
// the goal is to practice parameterised testing
// you don't need to use a spreadsheet (yet)

public class DefectTest {
    @Test(dataProvider = "")
    public void isValidReturnsFalseForInvalidDefects(String name, String summary, String details) {
        // comment these out once your data provider method works
        System.out.println("Test case");
        System.out.println("\tname: " + name);
        System.out.println("\tsummary: " + summary);
        System.out.println("\tdetails: " + details);
        // add your test code below
    }

    @DataProvider(name = "")
    public Object[][] invalidDefectData() {
        // return a 2D array of inputs and expected urls
        // you can hard code it for now
    }
}
