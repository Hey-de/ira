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
	"io"
	"net/http"
	"os"
	"os/exec"
	"runtime"

	"github.com/spf13/cobra"
)

func InstallExe(which string) bool {
	if runtime.GOOS != "windows" {
		return false
	}
	var exeTemp = getTemporaryPath() + which + ".exe"
	file, err := os.OpenFile(exeTemp, os.O_CREATE|os.O_APPEND, os.ModePerm)
	cobra.CheckErr(err)
	if url, ok := repos["exe"][which]; ok {
		resp, err := http.Get(url)
		cobra.CheckErr(err)
		defer resp.Body.Close()
		_, err = io.Copy(file, resp.Body)
		cobra.CheckErr(err)
		cmd := exec.Command(exeTemp)
		cobra.CheckErr(cmd.Run())
		return true
	} else {
		return false
	}
}

var installExeCmd = &cobra.Command{
	Use:   "install-exe",
	Short: "Install Windows program",
	Long:  ``,
	Args:  cobra.MinimumNArgs(1),
	Run: func(cmd *cobra.Command, args []string) {
		InstallExe(args[0])
	},
}

func init() {
	rootCmd.AddCommand(installExeCmd)

}
