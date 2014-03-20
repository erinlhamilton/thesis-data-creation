package thesisDB;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class InsertWKT {
	  public static void main( String args[] )
	  {
	    Connection c = null;
	    Statement stmt = null;
	    try {
	      Class.forName("org.sqlite.JDBC");
	      c = DriverManager.getConnection("jdbc:sqlite:path/to/your/database/wktData2.db");
	      c.setAutoCommit(false);
	      System.out.println("Opened database successfully");

	      stmt = c.createStatement();
	      String[] fileArray = {"Points", "Lines", "Polygons", "PolygonsA", "PolygonsB"};
	    
	      for (int i = 0; i < fileArray.length; i++){
	      File f = new File("path/to/your/wkt/data/toDB/"+fileArray[i]);
		  File[] list = f.listFiles();
		  for (File file : list){
	    	  //Open the file for reading
	    	int line = 0;
	          BufferedReader br = new BufferedReader(new FileReader(file.getPath()));
	          String fileName = file.getName();
	          String fileNumber = fileName.replace(".txt", "");
	          while (line < 1) { // while loop begins here
	        	  String thisLine = br.readLine();
	        	  String sql2 = "INSERT INTO " + fileArray[i] +"("+fileArray[i]+"ID, "+fileArray[i]+"WKT) " +
	        	  "VALUES (" + fileNumber + ", '" + thisLine + "')";
	        	  stmt.executeUpdate(sql2);
	        	  System.out.println(fileNumber);
	              line++;
	          }
	          br.close();
	        }
	      }
		  
	      stmt.close();
	      c.commit();
	      c.close();
	    } catch ( Exception e ) {
	      System.err.println( e.getClass().getName() + ": " + e.getMessage() );
	      System.exit(0);
	    }
	    System.out.println("Tables successfully populated");
	  }
}
