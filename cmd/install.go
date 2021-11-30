package cmd

import (
	"encoding/json"
	"fmt"
	"os"

	"github.com/spf13/cobra"
)

// installCmd represents the install command
var installCmd = &cobra.Command{
	Use:   "install",
	Short: "install a package",
	Long:  ``,
	Args:  cobra.MinimumNArgs(1),
	Run: func(cmd *cobra.Command, args []string) {
		if _, ok := repos["bpak"]; ok {
			cats := repos["bpak"]
			fmt.Printf("cats: %v\n", cats)
		} else {
			if repos == nil {
				repos = make(map[string]map[string]string)
			}
			repos["bpak"] = make(map[string]string)
			repos["bpak"]["core"] = "https://github.com/BIQ-Cat/core"
			toWrite, err := json.Marshal(repos)
			cobra.CheckErr(err)
			println(path)
			cobra.CheckErr(os.WriteFile(path, toWrite, os.ModeAppend))
		}
	},
}

func init() {
	rootCmd.AddCommand(installCmd)
}
