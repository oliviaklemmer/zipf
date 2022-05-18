if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Compute zipf distribution")
    parser.add_argument("--in_folder", help="the input folder")
    parser.add_argument("--out_folder", help="the output folder")
    args = parser.parse_args()

    main(args)
