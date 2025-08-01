class TrieNode{
    Map<Character, TrieNode> children = new HashMap<>();
    boolean isEndOfWord = false;
}

class Solution {
    private TrieNode root = new TrieNode();

    private void insert(String word){
        TrieNode node = root;
        for(char ch: word.toCharArray()){
            node = node.children.computeIfAbsent(ch, c -> new TrieNode());
        }
        node.isEndOfWord = true;
    }

    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";

        for(String word: strs){
            insert(word);
        }

        StringBuilder prefix = new StringBuilder();
        TrieNode trie = root;
        while(trie.children.size() == 1 && !trie.isEndOfWord){
            char nextChar = trie.children.keySet().iterator().next();
            prefix.append(nextChar);
            trie = trie.children.get(nextChar);
        }
        return prefix.toString();
    }
}