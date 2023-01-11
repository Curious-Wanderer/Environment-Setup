#James Pais
#Simply sorts the array of numbers in ascending order.

def simplesort(arr):
    pointer2 = 1 #Leading pointer
    organized = False
    count = 0
    while organized is False:
        pointer1 = pointer2 - 1 #Back-line pointer
        if arr[pointer2] < arr[pointer1]:
            count += 1
            temp1 = arr[pointer2]
            temp2 = arr[pointer1]
            arr[pointer2] = temp2
            arr[pointer1] = temp1
            if pointer2 == len(arr) - 1:
                if count == 0:
                    organized = True
                    print("Sorting Complete.")
                    print("Sorted Array: ", arr)
                else:
                    pointer2 *= 0
                    pointer2 += 1
                    count *= 0
            else:
                pointer2 += 1
        elif arr[pointer2] > arr[pointer1]:
            if pointer2 == len(arr) - 1:
                if count == 0:
                    organized = True
                    print("Sorting Complete.")
                    print("Sorted Array: ", arr)
                else:
                    pointer2 *= 0
                    pointer2 += 1
                    count *= 0
            else:
                pointer2 += 1

arr1 = [
    61, 241, 678, 1076, 1188, 1305, 1375, 2097, 2452, 2565, 2586, 2664, 3515, 3860, 4234, 4953, 4992, 5115,
    5238, 5409, 6625, 6716, 7284, 7356, 7612, 7739, 8736, 10, 37, 60, 62, 117, 121,
    150, 240, 299, 303, 315, 322, 342, 344, 422, 457, 549, 615, 677, 760, 1075, 1182, 1183, 1184,
    1185, 1186, 1187, 1189, 1190, 1191, 1192, 1193, 1194, 1195, 1196, 1197, 1198, 1199, 1200, 1201, 1202,
    1203, 1210, 1211, 1212, 1213, 1214, 1215, 1216, 1217, 1218, 1219, 1220, 1221, 1222, 1223, 1224, 1225,
    1226, 1227, 1228
]
simplesort(arr1)