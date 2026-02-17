def dfs_iterative(graph, start_vertex_id):

    if start_vertex_id not in graph: #vertex var mı kontrol ediyoruz
        return None
    
    
    visited = [] # Ziyaret edilenler (Sıralı tutmak için liste)
    visited_set = set() 
    stack = [start_vertex_id] # Python listesi Stack (LIFO) olarak kullanılır
    
    # Başlangıç düğümünü işaretleyelim
    visited.append(start_vertex_id)
    visited_set.add(start_vertex_id)  #ekleme yapalım 
    
    while stack: #stack boş değil ise 
        current_id = stack.pop() # Yığının en üstündekini al
        
        # Komşuları gezelim 
        # graph[current_id] komşuların listesini döndürür
        for neighbor in graph.get(current_id, []):
            if neighbor not in visited_set:
                # Komşuyu ziyaret edildi işaretle
                visited.append(neighbor)
                visited_set.add(neighbor)  #ekleme yapalım 
                
                # Mevcut düğümü geri dönmek için sakla 
                stack.append(current_id)
                # Yeni komşuyu yığına ekle (Derine gitmek için)
                stack.append(neighbor)
                
                #  İlk bulduğun komşuda derine dal
                break 
                
    return visited

# Örnek Kullanımı (Graf Yapısı)
my_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS Ziyaret Sırası:", dfs_iterative(my_graph, 'A'))