set_2016 = set(line.strip() for line in open('2016_orgs.txt'))
set_2017 = set(line.strip() for line in open('2017_orgs.txt'))
set_2018 = set(line.strip() for line in open('2018_orgs.txt'))
set_2019 = set(line.strip() for line in open('2019_orgs.txt'))
set_2020 = set(line.strip() for line in open('2020_orgs.txt'))

diff_1617 = set_2016.intersection(set_2017)
diff_1718 = diff_1617.intersection(set_2018)
diff_1819 = diff_1718.intersection(set_2019)
diff_1620 = diff_1819.intersection(set_2020)

# print(set_2016)
remain = []
for org in diff_1620:

    remain.append(org)
    print(org)
# print(len(remain))
# print(diff_1620)
