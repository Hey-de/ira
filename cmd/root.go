/*
Copyright © 2021 NAME HERE <EMAIL ADDRESS>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/
package cmd

import (
	"encoding/json"
	"io/ioutil"
	"os"
	"runtime"

	"github.com/spf13/cobra"
)

var path string

func getTemporaryPath() string {
	retPath, err := os.UserHomeDir()
	cobra.CheckErr(err)
	if runtime.GOOS == "windows" {
		retPath += "\\AppData\\iraCache\\"
	} else {
		retPath += "/.iraCache/"
	}
	_ = os.Mkdir(retPath, os.ModePerm)
	return retPath
}
func newCatRepo(file *os.File) {
	if repos == nil {
		repos = make(map[string]map[string]string)
	}
	repos["bpak"] = make(map[string]string)
	repos["bpak"]["core"] = "https://github.com/BIQ-Cat/core"
	repos["exe"] = make(map[string]string)
	repos["exe"]["git"] = "https://github.com/git-for-windows/git/releases/download/v2.34.1.windows.1/Git-2.34.1-64-bit.exe"
	toWrite, err := json.Marshal(repos)
	cobra.CheckErr(err)
	println(path)
	_, err = file.Write(toWrite)
	cobra.CheckErr(err)
}

// rootCmd represents the base command when called without any subcommands
var rootCmd = &cobra.Command{
	Use:   "ira",
	Short: "A package manager for Windows, Mac OS & Linux",
	Long: `A cross-platform package manager brought to you by BIQ
	Here you may install many applications. As a differency between
	another PMs and IRA in compatibility with Snap/Flatpak, WSL, brew,
	source code and more

	How to use?
	Example:
	* ira install vscode - Installing Visual Studio Code
	* ira remove steam - Removing Steam
	* ira append gui - Add IRA command 'gui'
	* ira recompile - Recompilling IRA PM from source code
	`,
}
var repoFile string
var repos map[string]map[string]string

func Execute() {
	initRepo()
	cobra.CheckErr(rootCmd.Execute())
}

func init() {
	rootCmd.PersistentFlags().StringVarP(&repoFile, "catsfile", "c", "", "File with cats (Default $HOME/.ira.json)")
}
func initRepo() {
	println(repoFile)
	if repoFile == "" {
		println("a")
		var err error
		path, err = os.UserHomeDir()
		cobra.CheckErr(err)
		println(path)
		if runtime.GOOS == "windows" {
			path += "\\AppData\\"
		} else {
			path += "/"
		}
		path += ".ira.json"
		println(path)
	} else {
		path = repoFile
	}
	file, err := os.OpenFile(path, os.O_CREATE|os.O_APPEND, os.ModePerm)
	cobra.CheckErr(err)
	data, err := ioutil.ReadAll(file)
	cobra.CheckErr(err)
	if string(data) == "" {
		newCatRepo(file)
	} else {
		cobra.CheckErr(json.Unmarshal(data, &repos))
	}
}
