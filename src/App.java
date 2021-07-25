import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class App extends Application {

    @Override
    public void start(Stage stage) throws Exception{
		FXMLLoader loader = new FXMLLoader(getClass().getResource("Scene.fxml"));
		loader.setController(new SceneController());
        
		Parent root = loader.load();


		stage.setScene(new Scene(root));
    stage.setTitle("Fake News Detector 1.0 - Don't Get Fooled!!");
		stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }

}