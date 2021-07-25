import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.text.Text;

import java.util.*; 
import java.io.*;

public class SceneController {

    @FXML
    private Text display;

    @FXML
    private Button submitBtn;

    @FXML
    private TextField txtField;

    @FXML
    void clearTxt(ActionEvent event) {
        txtField.clear();
        display.setText("");
    }

    @FXML
    void runPythonScript(ActionEvent event) {
        String result = "";
        String news = txtField.getText();
        try{    
            FileWriter fw=new FileWriter("news.txt");    
            fw.write(news);    
            fw.close();    
        }
        catch(Exception e){
            System.out.println(e);
        }  
        
        //run python script taking input from news.txt

       try{
            List<String> commands = new ArrayList<String>();
            commands.add("python"); // command
            commands.add("model.py");
            ProcessBuilder pb = new ProcessBuilder(commands);
            Process p = pb.start();
            p.waitFor();
        }catch(Exception e){
            e.printStackTrace();
        }

        try{
            File file = new File("results.txt");
            Scanner sc;
            sc = new Scanner(file);
            while (sc.hasNextLine()){
                result += sc.nextLine();
            }
            sc.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        display.setText(result);

    }

}
