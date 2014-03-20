package thesisDB;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class CreateTable {
	 public static void main( String args[] )
	  {
		 Connection c = null;
		 Statement stmt = null;
	    try {
	      Class.forName("org.sqlite.JDBC");
	      c = DriverManager.getConnection("jdbc:sqlite:path/to/your/database/wktData.db");
	      System.out.println("Opened database successfully");
	   
	      stmt = c.createStatement();
	      String sql1 = "CREATE TABLE Points " + 
	    		"(PointsID INTEGER PRIMARY KEY NOT NULL," +
	    		"PointsWKT BLOB)";
	      
	      stmt.executeUpdate(sql1);
	      System.out.println("Points Table Created");
	      
	      String sql2 = "CREATE TABLE Polygons " + 
	    		"(PolygonsID INTEGER PRIMARY KEY NOT NULL," +
	    		"PolygonsWKT BLOB)";
	      
	      stmt.executeUpdate(sql2);
	      System.out.println("Polygons Table Created");
	      
	      String sql3 = "CREATE TABLE Lines " + 
	    		"(LinesID INTEGER PRIMARY KEY NOT NULL," +
	    		"LinesWKT BLOB)";
	      
	      stmt.executeUpdate(sql3);
	      System.out.println("Lines Table Created");
	      
	      String sql4 = "CREATE TABLE PolygonsA " + 
	    		"(PolygonsAID INTEGER PRIMARY KEY NOT NULL," +
	    		"PolygonsAWKT BLOB)";
	      
	      stmt.executeUpdate(sql4);
	      System.out.println("PolyA Table Created");
	      
	      String sql5 = "CREATE TABLE PolygonsB " + 
		    		"(PolygonsBID INTEGER PRIMARY KEY NOT NULL," +
		    		"PolygonsBWKT BLOB)";
		      
		      stmt.executeUpdate(sql5);
		      System.out.println("PolyB Table Created");
	      
	      String sql6 = "CREATE TABLE Metadata " + 
 		  		"(MID INT PRIMARY KEY NOT NULL," +
 		  		"Date TEXT," +
 		  		"Browser Text, " +
 		  		"OperatingSystem Text," +
 		  		"Hardware Text)";
	      
	      stmt.executeUpdate(sql6);
	      System.out.println("Metadata Table Created");
	      
	     String sql7 = "CREATE TABLE Results " +
	     "(RowID INTEGER PRIMARY KEY AUTOINCREMENT," +
		  "ID INTEGER NOT NULL," +
		  "Platform TEXT," +
		  "Geoprocess Text," +
		  "DataType Text," +
		  "InputBytes INTEGER," +
		  "InputNodes INTEGER," +
		  "ServerDataMS DOUBLE," +
		  "InputParseMS DOUBLE," +
		  "GeoprocessMS DOUBLE," +
		  "OutputParseMS DOUBLE," +
		  "TotalTimeMS DOUBLE," +
		 "OutputBytes INTEGER," +
		  "OutputNodes INTEGER)";
	    		 
	   	      stmt.executeUpdate(sql7);
	   	      System.out.println("Results Table Created");

	        String sql8 = "CREATE TABLE Network " +
	   	      "(RowID INTEGER PRIMARY KEY AUTOINCREMENT," +
	    		  "ID INTEGER NOT NULL," +
	    		  "Latency INTEGER," +
	    		 	"LatError DOUBLE," +
	    		  "Bandwidth INTEGER," +
	    		  "BwError DOUBLE)";
	   	      
		      stmt.executeUpdate(sql8);
		      System.out.println("Network Table Created");

	      stmt.close();
	      c.close();

   } catch ( Exception e ) {
     System.err.println( e.getClass().getName() + ": " + e.getMessage() );
     System.exit(0);
   }
   System.out.println("Database successfully created.");
 }
}
