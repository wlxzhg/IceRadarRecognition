module xidianRadar {
	sequence<int> IntList;
	sequence<IntList> IntIntList;

	interface RadarUtil{
		IntList recognitionRadar(IntIntList r);
	};
};