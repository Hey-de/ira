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
	"io/ioutil"
	"os"
	"runtime"

	"github.com/spf13/cobra"
	yaml "gopkg.in/yaml.v3"
)

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
	cobra.CheckErr(rootCmd.Execute())
	initRepo()
}

func init() {
	rootCmd.PersistentFlags().StringVarP(&repoFile, "catsfile", "c", "", "File with cats (Default $HOME/.ira.yaml)")
}
func initRepo() {
	var path string
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
		path += ".ira.yml"
		println(path)
	} else {
		path = repoFile
	}
	file, err := os.OpenFile(path, os.O_CREATE|os.O_APPEND, os.ModePerm)
	cobra.CheckErr(err)
	if runtime.GOOS == "windows" {

	}
	data, err := ioutil.ReadAll(file)
	cobra.CheckErr(err)
	cobra.CheckErr(yaml.Unmarshal(data, repos))
}
