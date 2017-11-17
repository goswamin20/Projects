package com.designer.dbservice.model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name="products", catalog="designer")
public class Product {
	
	@Id
	@GeneratedValue(strategy=GenerationType.AUTO)
	@Column(name="productId")
	private int productId;
	
	@Column(name="productName")
	private String productName;
	
	@Column(name="productPrice")
	private double productPrice;
	
	@Column(name="productCategory")
	private String productCategory;
	
	public Product(){
		
	}
	public Product(Product p) {
		this.productCategory=p.productCategory;
		this.productName=p.productName;
		this.productPrice=p.productPrice;
	}
	

	public int getProductId() {
		return productId;
	}

	public void setProductId(int productId) {
		this.productId = productId;
	}

	public String getProductName() {
		return productName;
	}

	public void setProductName(String productName) {
		this.productName = productName;
	}

	public double getProductPrice() {
		return productPrice;
	}

	public void setProductPrice(double productPrice) {
		this.productPrice = productPrice;
	}

	public String getProductCategory() {
		return productCategory;
	}

	public void setProductCategory(String productCategory) {
		this.productCategory = productCategory;
	}

	@Override
	public String toString() {
		return "Product [productId=" + productId + ", productName=" + productName + ", productPrice=" + productPrice
				+ ", productCategory=" + productCategory + "]";
	}
	
	
}
