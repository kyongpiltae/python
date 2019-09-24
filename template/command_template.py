import os,sys,getopt,datetime

def main(argv):
    # Set default value of parameter
    FILE_NAME = argv[0]

    data_path = ''
    result_path = ''

    # Get parameter from command line
    try:
        opts,etc = getopt.getopt(argv[1:],"hd:r:",["help","data_path=","result_path="])
    except getopt.GetoptError:
        print('parsing error', opts)
        print(FILE_NAME,"-d <data path> -r <result path and name> ")
        sys.exit()
    
    #print(opts)
    for opt, arg in opts:
        if opt in ('-h',"--help"):
            print(FILE_NAME,"-d <data path> -r <result path and name> ")
            sys.exit()
        
        elif opt in ("-d","--data_path"):
            data_path = arg
            print("datapath is ->", data_path)

        elif opt in ("-r","--result_path"):
            result_path = arg
            print("result_apath is ->", result_path)
            #if( not os.path.exists(SavePath)):
            #    os.makedirs(SavePath)
        
    if len(data_path) < 2: # Mandotory check
        print(FILE_NAME, "-d option(data path option) is mandatory")
        sys.exit(2)


if __name__ == '__main__':
    main(sys.argv)