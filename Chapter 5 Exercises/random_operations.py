import random


def random_sampling(k, A):
    for i in range(k):
        ind = random.randint(i, len(A)-1)
        A[ind], A[i] = A[i], A[ind]
    return A[:k]

# print(random_sampling(3, [1,2,3,4,5]))

reads = []
count = 0

def online_random_sample(k, read):
    global reads
    global count

    if len(reads) < k:
        reads.append(read)
        count += 1

    else:
        count += 1
        prob_replace = k/count
        x = random.uniform(0, 1)
        if x < prob_replace:
            reads[random.choice(range(k))] = read
        else:
            pass

    print(reads, count)

# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
#
# for a in alphabet:
#     online_random_sample(2, a)

def compute_random_permutation(n):
    permutation = list(range(n))
    return random_sampling(n, permutation)

# perms = []
# for x in range(90):
#     this_perm = compute_random_permutation(4)
#     if this_perm not in perms:
#         perms.append(this_perm)
#     else:
#         print("Repeat: ", this_perm)
#
# print(len(perms))


def random_subset(n, k):
    subset = {}
    for i in range(k):
        x = random.randint(0, n)
        rand_val = subset.get(x, x)
        i_val = subset.get(i, i)
        subset[i] = rand_val
        subset[x] = i_val

    return [subset[a] for a in range(k)]

print(random_subset(100, 10))
