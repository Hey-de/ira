package cmd

import (
	"fmt"

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
		}
		// } else {
		// 	// repos["bpak"] = make(map[string]string)
		// 	repos["bpak"]["core"] = "https://github.com/BIQ-Cat/core"
		// 	toWrite, err := yaml.Marshal(repos)
		// 	cobra.CheckErr(err)
		// 	cobra.CheckErr(os.WriteFile(path, toWrite, os.ModePerm))
		// }
	},
}

func init() {
	rootCmd.AddCommand(installCmd)
}
