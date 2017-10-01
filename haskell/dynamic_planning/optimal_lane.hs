{- Dynamic Plannning sample from alogorithm introduction -}
data StartLane = StartLane {startA :: Int, firstA :: Int, startB :: Int, firstB :: Int} deriving (Show)
data EndLane = EndLane {endA :: Int, endB :: Int} deriving (Show)
data Section = Section {timeA :: Int, crossAtoB :: Int, timeB :: Int, crossBtoA :: Int} deriving (Show)
type Sections = [Section]
data Label = A | B | End deriving (Show)
type Path = [(Label, Int, Int)] -- (lane Label, time to move to the lane, time to take at the lane)


startLane :: StartLane
startLane = StartLane 2 7 4 8


endLane :: EndLane
endLane = EndLane 3 2


toEndLane :: Sections
toEndLane = [ Section 9 2 5 2,
              Section 3 3 6 1,
              Section 4 1 4 2,
              Section 8 3 5 2,
              Section 4 4 7 1
            ]


calcFirstLane :: StartLane -> (Path, Path)
calcFirstLane (StartLane stA fstA stB fstB) =
    ([(A, stA, fstA)], [(B, stB, fstB)])


calcMoveTime :: Path -> Int
calcMoveTime = sum . map takeSecond
    where takeSecond :: (a, b, c) -> b
          takeSecond (_, y, _) = y


calcTakeTime :: Path -> Int
calcTakeTime = sum . map takeThird
    where takeThird :: (a, b, c) -> c
          takeThird (_, _, z) = z


stepLane :: (Path, Path) -> Section -> (Path, Path)
stepLane (pathA, pathB) (Section tmA crsAtoB tmB crsBtoA) =
    let totalTimeA = calcMoveTime pathA + calcTakeTime pathA
        totalTimeB = calcMoveTime pathB + calcTakeTime pathB
        forwardATime = totalTimeA + tmA
        crossBtoATime = totalTimeB + crsBtoA + tmA
        forwardBTime = totalTimeB + tmB
        crossAtoBTime = totalTimeA + crsAtoB + tmB
        newPathA = if forwardATime <= crossBtoATime
                       then (A, 0, tmA) : pathA
                       else (A, crsBtoA, tmA) : pathB
        newPathB = if forwardBTime <= crossAtoBTime
                       then (B, 0, tmB) : pathB
                       else (B, crsAtoB, tmB) : pathA
    in (newPathA, newPathB)


calcOptimalPath :: Sections -> StartLane -> EndLane -> (Path, Int)
calcOptimalPath sections start (EndLane a b) =
    let (candidatePathA, candidatePathB) = foldl stepLane (calcFirstLane start) sections
        totalTimeA = calcMoveTime candidatePathA + calcTakeTime candidatePathA + a
        totalTimeB = calcMoveTime candidatePathB + calcTakeTime candidatePathB + b
        bestPath = if totalTimeA <= totalTimeB
                       then reverse ((End, a, 0) : candidatePathA)
                       else reverse ((End, b, 0) : candidatePathB)
    in (bestPath, calcMoveTime bestPath + calcTakeTime bestPath)
