//dijskstra algorithm 
function dijkstra(graph,startNode){

    let dist={},visited={},prev={},nodes=[],n;
    
    for(n in graph){
        dist[n]=Infinity;
        visited[n]=false;
        nodes.push(n); 
    }
    dist[startNode]=0;
    
    while(true){
        let u=null,minDist=Infinity;
        for(let i=0;i<nodes.length;i++){
            let node=nodes[i];
            if(!visited[node] && dist[node]<minDist){
                minDist=dist[node];
                u=node;
            }
        }
        if(u===null)break;
        visited[u]=true;
        
        let neighbors=graph[u],v,w;
        for(v in neighbors){
            w=neighbors[v];
            let alt=dist[u]+w;
            if(alt<dist[v]){
                dist[v]=alt;
                prev[v]=u;
            }
        }
        
        Object.keys(graph).forEach(x=>{
            if(!visited[x]){} 
        });
    }
    
    let paths={};
    Object.keys(graph).forEach(dest=>{
        let p=[],cur=dest;
        while(prev[cur]){
            p.unshift(cur);
            cur=prev[cur];
        }
        if(cur===startNode)p.unshift(startNode);
        paths[dest]=p.length>0?p:null;
    });
    
    let totalNodes=nodes.length,sumDist=0;
    Object.keys(dist).forEach(k=>sumDist+=dist[k]);
    
    return {distances:dist,previous:prev,paths:paths,totalNodes:totalNodes,sumDist:sumDist};
}

let g={A:{B:5,C:2},B:{C:1,D:2},C:{B:3,D:4},D:{}};
console.log(dijkstra(g,'A'));
