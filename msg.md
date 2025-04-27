I want you to act as a professional Android app Java software engineer and as Android Studio. Your role as a software engineer is to review my code and ensure it adheres to clean code guidelines, such as readability, simplicity, and maintainability. You should ensure proper use of variables, methods, and modularization while removing redundant code. As Android Studio, your role is to import necessary classes, fix typos, format the code, and ensure its validity. When I provide code, you must:
', '
', 'Provide only the corrected and formatted code, without explanations.
', 'Summarize what you improved in the code in a concise manner after providing the corrected version.
', If you're ready, here is my first code:
package com.jdevoc.ShoppingCart;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import java.util.List;

public class CartListFragment extends Fragment{
  private RecyclerView  mCartRecyclerView;
  private CartAdapter mAdapter;

  @Override
  public View onCreateView(LayoutInflater inflater, ViewGroup container,Bundle savedInstanceSte){
    View view = inflater.inflate(R.layout.fragment_cart_list,container,false);
    mCartRecyclerView = (RecyclerView) view.findViewById(R.id.cart_recycler_view);
    mCartRecyclerView.setLayoutManager(new LinearLayoutManager(getActivity()));
    updateUI();
    return view;
  }
  private void updateUI(){
    CartLab cartLab = CartLab.get(getActivity());
    List<Item> items= cartLab.getItems();
    mAdapter = new CartAdapter(items);
    mCartRecyclerView.setAdapter(mAdapter);
  }
  private class CartHolder extends RecyclerView.ViewHolder{
    public CartHolder(LayoutInflater inflater, ViewGroup container){
      super(inflater.inflate(R.layout.list_item_cart,container,false));
    }
  }

  private class CartAdapter extends RecyclerView.Adapter<CartHolder>{
    private List<Item> mItems;
    public CartAdapter(List<Item> items){
      mItems=items;
    }
@Override
        public CartHolder onCreateViewHolder(ViewGroup parent, int viewType) {
            LayoutInflater layoutInflater = LayoutInflater.from(getActivity());
            return new CartHolder(layoutInflater, parent);
        }
    @Override
    public void onBindViewHolder(CartHolder holder, int position){
    }
    @Override
    public int getItemCount(){
      return mItems.size();
    }
  }
}