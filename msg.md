Explain the following code , i was kinda still coding but then something distructed me and i don't know how the things here work, iam learning from a textbook. Am a beginner.
package com.jdevoc.ShoppingCart;

import android.os.Bundle;
import android.app.Fragment;

import android.widget.Button;
import android.widget.EditText;
import android.widget.CheckBox;
import android.widget.TextView;
import android.widget.CompoundButton;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import android.text.Editable;
import android.text.TextWatcher;

import java.lang.CharSequence;

public class CartFragment extends Fragment{
  private Item mItem;
  private Button mShopping_date_button;
  private CheckBox mIs_already_shopped_checkbox;
  private  EditText mFood_type_text_entry;

  @Override
  public void onCreate(Bundle savedInstanceState){
    super.onCreate(savedInstanceState);
    mItem = new Item();
  }
  @Override
  public View onCreateView(LayoutInflater inflater,ViewGroup container,Bundle savedInstance){
    View v = inflater.inflate(R.layout.fragment_cart,container,false);

    mShopping_date_button = (Button) v.findViewById(R.id.shopping_date);
    mIs_already_shopped_checkbox = (CheckBox) v.findViewById(R.id.is_already_shopped);
    mFood_type_text_entry = (EditText) v.findViewById(R.id.food_type);

    mFood_type_text_entry.addTextChangedListener(new TextWatcher(){
      @Override
      public void beforeTextChanged(CharSequence sequence,int start,int count, int after){
      }
      @Override
      public void onTextChanged(CharSequence sequence,int start,int before,int count){
        mItem.setName(sequence.toString());
      }
      @Override
      public void afterTextChanged(Editable s){}
    });
  mShopping_date_button.setText(mItem.getDate().toString());
  mShopping_date_button.setEnabled(false);

  mIs_already_shopped_checkbox.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener(){
    @Override
    public void onCheckedChanged(CompoundButton buttonView, boolean isChecked){
      mItem.setIsShopped(isChecked);
    }
  });
  return v;
  }
}