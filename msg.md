In this code can you explain why i have to test whether the fragment is equal to null, does this work in that if the fm.findFragmentById(id) doesn't find the fragment corresoonding to the id it should create it?. All am not getting is why the do i check for null, when the id actually already exists in the xml files set as the view in the onCreate. Is it the fragment's existance in the activity rather than in xml that causes it to be null? Also why call beginTransaction().add(id, fragment) is this adding the fragment into view or adding it to fragmentManager list
package com.jdevoc.ShoppingCart;

import android.os.Bundle;
import android.app.Activity;
import android.app.Fragment;
import android.app.FragmentManager;

public class ShoppingCartActivity extends Activity{

  @Override
  protected void onCreate(Bundle savedInstanceState){
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_shoppingcart);

    FragmentManager fm =getFragmentManager();
    Fragment fragment = fm.findFragmentById(R.id.cart_fragment_container);
    if (fragment==null){
      fragment = new CartFragment();
      fm.beginTransaction()
        .add(R.id.cart_fragment_container,fragment)
        .commit();
    }
  }
}