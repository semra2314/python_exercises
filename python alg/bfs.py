from collections import deque

def bfs_iterative(graph, start_vertex_id):
    if start_vertex_id not in graph:    #vertex var mı kontrol ediyoruz
        return None
    
    visited = [] # Ziyaret sırasını tutan liste
    visited_set = set() # Hızlı kontrol için küme
    
    # BFS için Queue (Kuyruk) kullanılır. FİFO
    # deque, Python'da hızlı ekleme-çıkarma yapan bir kuyruk yapısıdır.pop yerine
    queue = deque([start_vertex_id])
    
    # Başlangıç düğümünü işaretle
    visited.append(start_vertex_id)
    visited_set.add(start_vertex_id)    #ekleme yapalım 
    
# kuyruk boş değil ise
    while queue:
        # Kuyruğun EN ÖNÜNDEKİ elemanı al (İlk giren ilk çıkar - FIFO)
        current_id = queue.popleft() 
        
        # Tüm komşuları tek seferde kontrol et
        for neighbor in graph.get(current_id, []):
            if neighbor not in visited_set:
                # Komşuyu ziyaret edildi işaretle
                visited.append(neighbor)
                visited_set.add(neighbor)  #ekleme yapalım 
                
                # Komşuyu kuyruğun sonuna ekle (Sırasını beklemesi için)
                queue.append(neighbor)
                
    return visited

# Örnek Kullanım
my_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("BFS Ziyaret Sırası:", bfs_iterative(my_graph, 'A'))

# Mantık : Önce komşuların hepsini ziyaret et, sonra onların komşularına geç.
# Tüm komşuları sırayla kuyruğa ekler ve katman katman gider.
# Level-order (Seviye sırası): BFS'nin düğümleri seviye seviye gezme biçimi.