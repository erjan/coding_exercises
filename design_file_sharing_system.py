'''
We will use a file-sharing system to share a very large file which consists of m small chunks with IDs from 1 to m.

When users join the system, the system should assign a unique ID to them. The unique ID should be used once for each user, but when a user leaves the system, the ID can be reused again.

Users can request a certain chunk of the file, the system should return a list of IDs of all the users who own this chunk. If the user receives a non-empty list of IDs, they receive the requested chunk successfully.


Implement the FileSharing class:

FileSharing(int m) Initializes the object with a file of m chunks.
int join(int[] ownedChunks): A new user joined the system owning some chunks of the file, the system should assign an id to the user which is the smallest positive integer not taken by any other user. Return the assigned id.
void leave(int userID): The user with userID will leave the system, you cannot take file chunks from them anymore.
int[] request(int userID, int chunkID): The user userID requested the file chunk with chunkID. Return a list of the IDs of all users that own this chunk sorted in ascending order.

'''


class FileSharing:

    def __init__(self, m: int):
        self.usersHaveChunk = defaultdict(set)
        self.chunkBelongToUser = defaultdict(set)
        self.nextID = 1

    def join(self, ownedChunks: List[int]) -> int:
        uid = self.nextID
        for i in itertools.count(uid+1):
            if i not in self.chunkBelongToUser:
                self.nextID = i
                break
        self.chunkBelongToUser[uid] = set(ownedChunks)
        for ch in ownedChunks:
            self.usersHaveChunk[ch].add(uid)
        return uid    

    def leave(self, userID: int) -> None:
        if userID < self.nextID:
            self.nextID = userID
        for ch in self.chunkBelongToUser[userID]:
            self.usersHaveChunk[ch].remove(userID)
        del self.chunkBelongToUser[userID]

    def request(self, userID: int, chunkID: int) -> List[int]:
        ans = sorted(self.usersHaveChunk[chunkID])        
        if ans:
            self.usersHaveChunk[chunkID].add(userID)
            self.chunkBelongToUser[userID].add(chunkID)
        return ans
