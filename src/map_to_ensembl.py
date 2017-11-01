import argparse
import requests

def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('file', help='filepath of symbol tsv')
    parser.add_argument('out', help='output filepath of ensembl id tsv')

    args = parser.parse_args()

    esembl_ids = []
    with open(args.file, 'r') as f:
        lines = f.readlines()
        for l in lines:
            r = requests.request(method='get', url='https://dr-sgc.kccg.garvan.org.au/_elasticsearch/_search', data='{"query": {"match" : {"symbol" : {"query" : "' + l.strip() +'"}}}}')
            print("**************************************************")
            print(l)
            print(r.json())
            esembl_ids.append(r.json()['hits']['hits'][0]['_id'])

    with open(args.out, 'w') as f:
        for i in esembl_ids:
            f.write(i)
            f.write('\n')
        # print(lines)


def ensembl(symbol):
    return ''


if __name__ == '__main__':
    main()
