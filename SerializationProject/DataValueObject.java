package JIMO.SerializationProject;

import java.io.Serializable;

public class DataValueObject implements Serializable {

  private String Customer;
  private String Business;
  transient private String contractID;
  transient private String passKeys;

  public void setCustomer(String customer) {
    this.Customer = customer;
  }

  public void setPassKeys(String passKeys) {
    this.passKeys = passKeys;
  }

  public void setBusiness(String business) {
    this.Business = business;
  }

  public void setContractID(String contractID) {
    this.contractID = contractID;
  }

  public String getPassKeys() {
    return passKeys;
  }

  public String getContractID() {
    return contractID;
  }

  public String getBusiness() {
    return Business;
  }

  public String getCustomer() {
    return Customer;
  }

  public String toString() {
    String value =
        "Customer :" + Customer + "Business :" + Business + "Passkeys: " + passKeys + "ContractID :"
            + contractID;
    return value;
  }

}
