Explain my code , i have forgotten how it works, am looking for understanding
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