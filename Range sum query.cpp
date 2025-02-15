void solve() {
    int n,q;
    cin>>n>>q;
    vector<long long > v(n+1,0);
    for (int i=1;i<n+1;i++){
        cin>>v[i];
        v[i]+=v[i-1];
    }
    long long  sum;
    for(int i=0;i<q;i++){
        int l,r;
        cin>>l>>r;
        
        cout<<v[r]-v[l-1]<<endl;
 
    }
 
 
 
}
