def compare_version(version1, version2):
    version1_split = version1.split('.')
    version2_split = version2.split('.')

    if len(version1_split) > len(version2_split):
        x_len = abs(len(version2_split) - len(version1_split))
        for i in range(x_len):
            version2_split.append('0')
    elif len(version2_split) > len(version1_split):
        y_len = abs(len(version1_split) - len(version2_split))
        for j in range(y_len):
            version1_split.append('0')
    for i in range(len(version1_split)):
        if int(version1_split[i]) > int(version2_split[i]):
            return 'version1 is greater...'
        elif int(version2_split[i]) > int(version1_split[i]):
            return 'version2 is greater...'


Version1 = "1.2.5"
Version2 = "0.0.1.2.5.6"
Output = compare_version(Version1, Version2)
print(Output)
