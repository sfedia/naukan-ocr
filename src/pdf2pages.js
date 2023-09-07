import { fromPath } from "pdf2pic";


function convertFile(sourcePath, lastPage, destFolder, picNamePrefix) {
    const options = {
        density: 100,
        saveFilename: picNamePrefix,
        savePath: `./${destFolder}`,
        format: "png",
        width: 600,
        height: 600
    };
    const convert = fromPath(sourcePath, options);

    for (let i = 1; i <= lastPage; i ++) {
        console.log(`Converting page ${i}`);
        convert(i, { responseType: "image" })
        .then((resolve) => {
            console.log(`Page ${i} is now converted as image`);

            return resolve;
        });
    }
}

convertFile("./Ненлюмкина 1985 Солнышко.pdf", 20, "nenl1985", "nenl1985-page")