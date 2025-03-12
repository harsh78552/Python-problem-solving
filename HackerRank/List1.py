def List_Manipulation(num):
	list_initialize = []
	for integer in range(1, num + 1):
		command_num = input().split()
		print(command_num)
		command = command_num[0]
		if command == "insert":
			list_initialize.insert(int(command_num[1]), int(command_num[2]))
		elif command == "print":
			print(list_initialize)
		elif command == "remove":
			list_initialize.remove(int(command_num[1]))
		elif command == "append":
			list_initialize.append(int(command_num[1]))
		elif command == "sort":
			list_initialize.sort(reverse=False)
		elif command == "pop":
			if list_initialize:
				list_initialize.pop()
		elif command == "reverse":
			list_initialize.reverse()


input_num_ = int(input())
List_Manipulation(input_num_)
