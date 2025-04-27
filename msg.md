I want you to act as a professional Android app Java software engineer and as Android Studio. Your role as a software engineer is to review my code and ensure it adheres to clean code guidelines, such as readability, simplicity, and maintainability. You should ensure proper use of variables, methods, and modularization while removing redundant code. As Android Studio, your role is to import necessary classes, fix typos, format the code, and ensure its validity. When I provide code, you must:
', '
', 'Provide only the corrected and formatted code, without explanations.
', 'Summarize what you improved in the code in a concise manner after providing the corrected version.
', If you're ready, here is my first code:
package com.jdevoc.List;

public class NamesAdapter extends RecyclerView.Adapter<NamesAdapter.ViewHolder>{
  private final String[] names;
  public static class ViewHolder extends RecyclerView.ViewHolder{
    private final TextView textView;
    public ViewHolder(View view){
      super(view);
      textView = (TextView) findViewById(R.id.textView);
      view.setOnClickListener(v->Toast.make(view.getContext(),"Hello",Toast.LENGTH_SHORT).show(););
    }
    public TextView getTextView(){
      return textView;
    }
  }
  public NamesAdapter(String[] n){
    this.name=n;
  }
  @Override
  public ViewHolder onCreateViewHolder(ViewGroup viewGroup,int viewType){
    View view = LayoutInflator.from(viewGroup.getContext()).inflate(R.layout.text_row_item,viewGroup,false);
    return new ViewHolder(view)
  }
  @Override
  public void onBindViewHolder(ViewGroup viewGroup,int position){
    ViewHolder.getTextView().setText(names[position]);
  }
  @Override
  public int getItemCount(){
    return names.length;
  }
}