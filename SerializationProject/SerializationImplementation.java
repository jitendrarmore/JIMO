package JIMO.SerializationProject;

import java.io.IOException;

public class SerializationImplementation {

  public static void main(String args[]) {
    DataValueObject dataValueObject = new DataValueObject();
    dataValueObject.setCustomer("Jitendra More");
    dataValueObject.setBusiness("Telecom");
    dataValueObject.setContractID("ZZZZZZ");
    dataValueObject.setPassKeys("!@wer#$");

    try {
      SerializationDemo.serialization("FileToSave.txt", dataValueObject);
      DataValueObject object = (DataValueObject) SerializationDemo
          .deSerialization("fileToSave.txt");
      System.out.println(object.toString());
    } catch (IOException exp) {
      exp.printStackTrace();
    } catch (ClassNotFoundException exp) {
      exp.printStackTrace();
    }
  }
}
